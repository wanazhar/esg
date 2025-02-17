# utils/validation.py
from pydantic import BaseModel, validator, root_validator
from typing import Dict, Optional
import re

class GlobalESGData(BaseModel):
    exchange_code: str
    symbol: str
    scores: Dict[str, float]
    sources: List[str]
    last_updated: str
    compliance_status: Dict[str, bool]
    
    @root_validator
    def validate_global_rules(cls, values):
        # Region-specific validation
        exchange = values.get('exchange_code')
        scores = values.get('scores', {})
        
        # Asian exchanges governance requirement
        if exchange in ['TSE', 'HKEX', 'SGX'] and scores.get('governance') is None:
            raise ValueError(f'{exchange} requires governance score disclosure')
            
        # European SFDR compliance
        if exchange in ['LSE', 'EURONEXT'] and not values['compliance_status'].get('SFDR'):
            raise ValueError('SFDR compliance not verified')
            
        return values
# utils/validation.py
class ESGValidationModel(RefinitivESGScores):
    @validator('esg_score')
    def validate_esg_range(cls, v):
        if not (0 <= v <= 100):
            raise ValueError('ESG score must be 0-100')
        return v
    
    @root_validator
    def validate_subcategory_relationships(cls, values):
        # Ensure subcategories sum to pillar scores
        env_sub = sum([values.get('resource_use',0), values.get('emissions',0), values.get('innovation',0)])
        if abs(env_sub - values['environmental_pillar']) > 1:
            raise ValueError('Environmental subcategories must sum to pillar score')
            
        # Similar checks for other pillars
        return values