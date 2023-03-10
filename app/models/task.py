from .db import db, environment

###############
# TASK MODEL:
###############

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(3000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    task_img_url = db.Column(db.String(1000))

    # RELATIONSHIPS:
    # users.id <--> tasks.user_id "one user can have many tasks"
    task_owner = db.relationship("User", back_populates="user_task")

    # reviews.task_id <--> tasks.id "one task can have many reviews"
    task_review = db.relationship("Review", back_populates="review_task", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "task_img_url": self.task_img_url
        }

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"


