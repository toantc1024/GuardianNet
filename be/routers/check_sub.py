from constant import Constants
from datetime import datetime

def check_subscription_status():
    try:
        current_time = datetime.utcnow()

        # Find all users with active subscriptions that have expired
        expired_users = Constants.USERS.find({
            "is_subscribed": True,
            "subscription_end": {"$lt": current_time}
        })

        # Update the subscription status of expired users
        for user in expired_users:
            Constants.USERS.update_one(
                {"_id": user["_id"]},
                {"$set": {"is_subscribed": False}}
            )

        print("Subscription statuses updated")

    except Exception as e:
        print(f"Error updating subscription statuses: {e}")
