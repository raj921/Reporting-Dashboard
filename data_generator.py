
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json

class SessionDataGenerator:
    def __init__(self):
        self.therapists = [
            {"id": "T001", "name": "Dr. Sarah Johnson", "rate": 150},
            {"id": "T002", "name": "Dr. Michael Chen", "rate": 175},
            {"id": "T003", "name": "Dr. Emily Rodriguez", "rate": 160},
            {"id": "T004", "name": "Dr. David Thompson", "rate": 180},
            {"id": "T005", "name": "Dr. Lisa Anderson", "rate": 155},
            {"id": "T006", "name": "Dr. James Wilson", "rate": 170},
        ]
        
        self.session_types = [
            "Individual Therapy",
            "Couples Therapy", 
            "Family Therapy",
            "Group Therapy",
            "Initial Consultation"
        ]
        
        self.session_statuses = [
            "Completed", "Cancelled", "No-Show", "Rescheduled"
        ]
        
        # Realistic probability weights
        self.status_weights = [0.75, 0.15, 0.08, 0.02]  # Most sessions completed
        
    def generate_sessions(self, num_sessions=500, start_date=None, end_date=None):
        
        
        if start_date is None:
            start_date = datetime.now() - timedelta(days=365)
        if end_date is None:
            end_date = datetime.now()
            
        sessions = []
        
        for i in range(num_sessions):
            # Random therapist
            therapist = random.choice(self.therapists)
            
            # Random date within range
            random_date = start_date + timedelta(
                days=random.randint(0, (end_date - start_date).days)
            )
            
            # Business hours (9 AM to 6 PM)
            hour = random.randint(9, 17)
            minute = random.choice([0, 30])  # Sessions start on hour or half-hour
            session_datetime = random_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # Skip weekends (optional - remove if weekend sessions are allowed)
            if session_datetime.weekday() >= 5:  # Saturday = 5, Sunday = 6
                continue
                
            # Session details
            session_type = random.choice(self.session_types)
            status = np.random.choice(self.session_statuses, p=self.status_weights)
            
            # Duration based on session type
            if session_type == "Initial Consultation":
                duration = 90
            elif session_type == "Couples Therapy" or session_type == "Family Therapy":
                duration = 60
            else:
                duration = 50
                
            # Calculate amount
            base_amount = therapist["rate"]
            if session_type == "Initial Consultation":
                amount = base_amount * 1.2  # 20% more for initial consult
            elif session_type == "Group Therapy":
                amount = base_amount * 0.6  # Group sessions cost less per person
            else:
                amount = base_amount
                
            # No payment if cancelled or no-show
            if status in ["Cancelled", "No-Show"]:
                amount = 0
                
            session = {
                "session_id": f"S{i+1:04d}",
                "therapist_id": therapist["id"],
                "therapist_name": therapist["name"],
                "client_id": f"C{random.randint(1, 200):03d}",
                "session_date": session_datetime.strftime("%Y-%m-%d"),
                "session_time": session_datetime.strftime("%H:%M"),
                "session_type": session_type,
                "duration_minutes": duration,
                "status": status,
                "amount": round(amount, 2),
                "notes": self._generate_notes(status)
            }
            
            sessions.append(session)
            
        return pd.DataFrame(sessions)
    
    def _generate_notes(self, status):
        """Generate realistic notes based on session status"""
        notes_templates = {
            "Completed": [
                "Session completed successfully",
                "Good progress noted",
                "Client engaged throughout session",
                "Homework assigned for next week",
                "Regular session, no concerns"
            ],
            "Cancelled": [
                "Client cancelled 24 hours in advance",
                "Cancelled due to illness",
                "Emergency cancellation",
                "Cancelled - family emergency",
                "Client requested reschedule"
            ],
            "No-Show": [
                "Client did not attend",
                "No advance notice given",
                "Third no-show this month",
                "Client not reachable",
                "Missed appointment"
            ],
            "Rescheduled": [
                "Rescheduled to next week",
                "Moved to different time slot",
                "Client requested different day",
                "Therapist availability conflict",
                "Mutual agreement to reschedule"
            ]
        }
        
        return random.choice(notes_templates.get(status, ["Standard session"]))
    
    def save_to_csv(self, df, filename="therapy_sessions.csv"):
        """Save the generated data to CSV"""
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return filename
    
    def save_to_json(self, df, filename="therapy_sessions.json"):
        """Save the generated data to JSON"""
        df.to_json(filename, orient="records", date_format="iso", indent=2)
        print(f"Data saved to {filename}")
        return filename

def main():
    """Generate sample data"""
    generator = SessionDataGenerator()
    
    # Generate data for the last year
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    
    df = generator.generate_sessions(
        num_sessions=800, 
        start_date=start_date, 
        end_date=end_date
    )
    
    # Save data
    generator.save_to_csv(df, "/Users/rajkumar/reporting dashboard/therapy_sessions.csv")
    generator.save_to_json(df, "/Users/rajkumar/reporting dashboard/therapy_sessions.json")
    
    # Print summary
    print(f"\nGenerated {len(df)} sessions")
    print(f"Date range: {df['session_date'].min()} to {df['session_date'].max()}")
    print(f"Therapists: {df['therapist_name'].nunique()}")
    print(f"Status distribution:\n{df['status'].value_counts()}")
    
    return df

if __name__ == "__main__":
    main()