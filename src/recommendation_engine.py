def generate_recommendations(customer):
    """
    Generate rule-based retention recommendations
    using customer characteristics.
    """

    recommendations = []

    if customer["Contract"] == "Month-to-month":
        recommendations.append(
            "Consider offering a suitable longer-term contract incentive."
        )

    if customer["tenure"] < 12:
        recommendations.append(
            "Consider an early-tenure retention offer or onboarding support."
        )

    if customer["OnlineSecurity"] == "No":
        recommendations.append(
            "Consider offering or highlighting an online security service."
        )

    if customer["TechSupport"] == "No":
        recommendations.append(
            "Consider offering targeted technical support assistance."
        )

    if customer["MonthlyCharges"] >= 80:
        recommendations.append(
            "Review pricing and perceived value; consider a targeted retention offer."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "No specific retention action identified by the current rules."
        )

    return recommendations


def generate_retention_plan(customer, churn_probability):
    """
    Generate a retention plan based on churn risk
    and customer characteristics.
    """

    recommendations = []

    if churn_probability < 0.40:
        recommendations.append(
            "Customer is currently low risk; continue regular engagement."
        )

    elif churn_probability < 0.70:
        recommendations.append(
            "Customer is medium risk; consider targeted retention engagement."
        )

    else:
        recommendations.append(
            "Customer is high risk; prioritize for retention intervention."
        )

    recommendations.extend(
        generate_recommendations(customer)
    )

    return recommendations