class HealthcheckManager:

    @staticmethod
    async def get_health_status():
        return {
            "success": True,
            "message": "API service is healthy"
        }
