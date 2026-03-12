from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

# Import the logic engine
from . import mapping_engine

# Initialize the FastAPI app with metadata for automatic documentation
app = FastAPI(
    title="Unicode to Plain Text API",
    description="A minimalist SaaS API to convert between specialized Unicode styles (bold, italic, fraktur, script, etc.) and standard plain text representation.",
    version="1.0.0",
)

class ConversionType(str, Enum):
    to_plain = "to_plain"
    to_unicode = "to_unicode"

class ConversionRequest(BaseModel):
    text: str = Field(..., description="The string to be converted.")
    conversion_type: ConversionType = Field(..., description="The direction of the conversion: 'to_plain' or 'to_unicode'.")
    target_style: Optional[str] = Field(None, description="Required only when conversion_type is 'to_unicode'. The specific style to apply: 'bold', 'italic', 'script', 'fraktur', 'monospace', or 'double_struck'.")

class ConversionResponse(BaseModel):
    original_text: str
    converted_text: str
    conversion_type: ConversionType
    applied_style: Optional[str] = None

@app.post("/convert", response_model=ConversionResponse, summary="Convert Text")
async def convert_text(request: ConversionRequest):
    """
    Bidirectional Conversion Endpoint.

    - If **conversion_type = "to_plain"**:
        Provide styled unicode text. It will strip out the formatting and return standard ASCII plaintext.
    - If **conversion_type = "to_unicode"**:
        Provide standard ASCII plaintext, and specify the `target_style`. It will return the decorated string.
    """
    
    if request.conversion_type == ConversionType.to_plain:
        result = mapping_engine.convert_to_plain(request.text)
        return ConversionResponse(
            original_text=request.text,
            converted_text=result,
            conversion_type=request.conversion_type,
            applied_style=None
        )
        
    elif request.conversion_type == ConversionType.to_unicode:
        if not request.target_style:
            raise HTTPException(status_code=400, detail="target_style is required when conversion_type is 'to_unicode'.")
        
        try:
            result = mapping_engine.convert_to_style(request.text, request.target_style)
            return ConversionResponse(
                original_text=request.text,
                converted_text=result,
                conversion_type=request.conversion_type,
                applied_style=request.target_style
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
