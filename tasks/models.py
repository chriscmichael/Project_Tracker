from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    project = models.ForeignKey(
        "projects.Project",
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        "auth.User", related_name="tasks", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

# from django.db import models

# COUNTRY_CHOICES =(
#     ("1","Ethiopia"),
#     ("2","Costa Rica"),
# )

# PROCESSING_CHOICES =(
#     ("1", "Washed"),
#     ("2", "Natural"),
#     ("3", "Black Honey"),
#     ("4", "Red Honey"),
#     ("5", "Yellow Honey"),
#     ("6", "White Honey"),
# )

# RATING_CHOICES = (
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ("4", "4"),
#     ("5", "5"),
# )

# class Cup (models.Model):
#     date_consumed = models.DateTimeField(auto_now=True)
#     roast_date = models.DateField()
#     country = models.CharField(
#         max_length = 50,
#         choices = COUNTRY_CHOICES,
#         default = '1'
#         )
#     process = models.CharField(
#         max_length = 15,
#         choices = PROCESSING_CHOICES,
#         default = '1'
#         )
#     description = models.TextField()
#     rating = models.CharField(
#         max_length = 3,
#         choices = RATING_CHOICES,
#         default = '1'
#         )

#     def __str__(self):
#         return self.date_consumed
