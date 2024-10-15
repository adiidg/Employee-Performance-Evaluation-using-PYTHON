# analytics.py
import matplotlib.pyplot as plt

def generate_performance_graph(reviews):
    employee_names = [review.employee.name for review in reviews]
    scores = [review.score for review in reviews]

    plt.figure(figsize=(10, 5))
    plt.bar(employee_names, scores, color='skyblue')
    plt.title('Employee Performance Scores')
    plt.xlabel('Employees')
    plt.ylabel('Performance Score')
    plt.ylim(0, 10)  # Assuming scores are out of 10
    plt.axhline(y=5, color='red', linestyle='--', label='Average Score')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
