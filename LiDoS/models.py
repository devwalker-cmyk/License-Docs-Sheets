from dataclasses import dataclass
from typing import Optional
import datetime

#6/30/2023

@dataclass
class LicenseKey:
    """A license key.

    Attributes :
    ----------
    - key : str
        - The license key.
    
    - expiration : Optional[datetime.date] = None 
        - The expiration date of the license key. If None, the key is considered non-expiring.
        
    - status : bool = False
        - The status of the license key. If True, the key is considered valid.
    
    -------
    Methods :
    -------
    is_expired() -> bool
        Check if the license key is expired.
    -------
    is_valid() -> bool
        Check if the license key is valid.
    -------
    is_active() -> bool
        Check if the license key is active.
    ...


    """
    key: str
    expiration: Optional[datetime.date] = None
    status: bool = False




    def is_expired(self) -> bool:
        """Check if the license key is expired.

        Returns
        -------
        bool
            True if the license key is expired, False otherwise.

        """
        if self.expiration is None:
            return False
        return self.expiration < datetime.date.today()
    
    def is_active(self) -> bool:
        """Check if the license key is active.

        Returns
        -------
        bool
            True if the license key is active, False otherwise.

        """
        return self.status and not self.is_expired()

    def is_valid(self) -> bool:
        """Check if the license key is valid.

        Returns
        -------
        bool
            True if the license key is valid, False otherwise.

        """
        return not self.is_expired()
    
    def __str__(self) -> str:
        return self.key
    
    def __repr__(self) -> str:
        return f"LicenseKey(key={self.key}, expiration={self.expiration})"
    

