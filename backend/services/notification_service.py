# FILE: backend/services/notification_service.py
# This service handles the logic for sending proactive alerts to users.
# For the hackathon, this is a conceptual service. In a real-world application,
# its methods would be triggered by a scheduled task runner (like Celery with Redis/RabbitMQ).

from typing import List, Dict

class NotificationService:
    """
    A service to manage sending notifications to users about scheme deadlines
    and changes in eligibility.
    """

    def send_deadline_reminder(self, user_email: str, scheme_name: str, deadline: str):
        """
        Sends a reminder about an upcoming application deadline.
        In a real app, this would use an email service (like SendGrid, Mailgun)
        or a push notification service (like Firebase Cloud Messaging).
        """
        subject = f"Reminder: Application Deadline for {scheme_name}"
        body = (
            f"Dear User,\n\n"
            f"This is a friendly reminder that the application deadline for the '{scheme_name}' "
            f"scheme is approaching on {deadline}.\n\n"
            f"Don't miss out on this opportunity!\n\n"
            f"Regards,\nThe SchemeSavvy Team"
        )
        
        # --- MOCK EMAIL SENDING ---
        print("--- SENDING EMAIL (MOCK) ---")
        print(f"TO: {user_email}")
        print(f"SUBJECT: {subject}")
        print(f"BODY: {body}")
        print("--------------------------")
        # --- END MOCK ---

        return {"status": "ok", "message": f"Deadline reminder for {scheme_name} sent to {user_email}."}

    def send_new_eligibility_alert(self, user_email: str, scheme_name: str, reason: str):
        """
        Notifies a user that they have become newly eligible for a scheme.
        """
        subject = f"Congratulations! You are now eligible for {scheme_name}"
        body = (
            f"Dear User,\n\n"
            f"Good news! Due to a recent change ({reason}), you are now eligible to apply for the "
            f"'{scheme_name}' scheme.\n\n"
            f"Log in to your SchemeSavvy dashboard to learn more and apply.\n\n"
            f"Regards,\nThe SchemeSavvy Team"
        )
        
        # --- MOCK EMAIL SENDING ---
        print("--- SENDING EMAIL (MOCK) ---")
        print(f"TO: {user_email}")
        print(f"SUBJECT: {subject}")
        print(f"BODY: {body}")
        print("--------------------------")
        # --- END MOCK ---

        return {"status": "ok", "message": f"New eligibility alert for {scheme_name} sent to {user_email}."}

    def run_daily_checks(self):
        """
        CONCEPTUAL: This method would be run once every 24 hours by a scheduler.
        It would query the database for all users and schemes to check for
        upcoming deadlines or changes in eligibility status.
        """
        print("\n--- RUNNING DAILY NOTIFICATION CHECKS (CONCEPTUAL) ---")
        
        # 1. Logic to find users whose 18th birthday is today.
        #    - Query: `SELECT * FROM users WHERE DATE_OF_BIRTH = TODAY - 18 YEARS`
        #    - For each user found, find schemes with `min_age: 18`.
        #    - Call `send_new_eligibility_alert(user.email, scheme.name, "you turned 18")`.
        print("Checking for users who turned 18 today...")
        # Mock finding a user
        self.send_new_eligibility_alert("user123@example.com", "Atal Pension Yojana", "you just turned 18")

        # 2. Logic to find schemes with deadlines in 7 days.
        #    - Query: `SELECT * FROM schemes WHERE application_deadline = TODAY + 7 DAYS`
        #    - For each scheme, find all eligible users.
        #    - Call `send_deadline_reminder(user.email, scheme.name, scheme.deadline)`.
        print("\nChecking for scheme deadlines approaching in 7 days...")
        # Mock finding a scheme
        self.send_deadline_reminder("user456@example.com", "Mukhya Mantri Yuva Swavalamban Yojana", "July 27, 2025")

        print("\n--- DAILY CHECKS COMPLETE ---")


# Create a single, reusable instance of the service.
notification_service = NotificationService()

# To demonstrate how it would work, you can uncomment the line below and run `python notification_service.py`
# if __name__ == "__main__":
#     notification_service.run_daily_checks()