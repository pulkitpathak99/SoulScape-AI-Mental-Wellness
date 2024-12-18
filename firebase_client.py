import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def log_user_activity(user_id, activity, mood, timestamp):
    """
    Logs user activity into the Firebase Firestore database.

    Args:
        user_id (str): Unique identifier for the user.
        activity (str): Activity the user is directed to.
        mood (str): Mood detected from the user's input.
        timestamp (datetime): Timestamp of the activity.

    Returns:
        None
    """
    activity_data = {
        "activity": activity,
        "mood": mood,
        "timestamp": timestamp
    }

    try:
        # Save the data into the Firestore collection
        db.collection("user_activities").document(user_id).collection("activities").add(activity_data)
        print(f"Activity logged for user {user_id}: {activity_data}")
    except Exception as e:
        print(f"Error logging activity: {e}")

def fetch_user_activities(user_id):
    """
    Fetches all logged activities for a given user from Firestore.

    Args:
        user_id (str): Unique identifier for the user.

    Returns:
        list: A list of activity dictionaries.
    """
    try:
        activities_ref = db.collection("user_activities").document(user_id).collection("activities")
        activities = activities_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
        return [activity.to_dict() for activity in activities]
    except Exception as e:
        print(f"Error fetching activities: {e}")
        return []