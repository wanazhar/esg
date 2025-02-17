# models/esg_metrics.py
from pydantic import BaseModel
from typing import Dict, Optional

class RefinitivESGScores(BaseModel):
    # Overall Scores
    esg_score: float
    environmental_pillar: float
    social_pillar: float
    governance_pillar: float
    
    # Environmental Subcategories
    resource_use: Optional[float]
    emissions: Optional[float]
    innovation: Optional[float]
    
    # Social Subcategories  
    workforce: Optional[float]
    human_rights: Optional[float]
    community: Optional[float]
    product_responsibility: Optional[float]
    
    # Governance Subcategories
    management: Optional[float]
    shareholders: Optional[float]
    csr_strategy: Optional[float]