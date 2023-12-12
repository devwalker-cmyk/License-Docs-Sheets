







class LicenseKeyNotFound(Exception):
    """Raised when the license key is not found in the database"""
    pass

class LicenseKeyExpired(Exception):
    """Raised when the license key is expired"""
    pass



class InvalidDateFormat(Exception):
    """Raised when the date format is invalid"""
    pass



class LicenseKeyNotActive(Exception):
    """Raised when the license key is not active"""
    pass