
def generate_query(country, donation_plans, start_date, end_date):
    donation_plans_str = ', '.join(f"'{plan}'" for plan in donation_plans)
    query = (
        "SELECT country, donation_plan, SUM(amount)"
        "FROM donation"
        f"WHERE country = '{country}'"
        f"AND donation_plan IN({donation_plans_str})"
        f"AND date BETWEEN '{start_date}' AND '{end_date}'"
        "GROUP BY donation_plan"
        )

    return query
