# Module 3: Core Calculation Logic

class ProfitCalculator:
    @staticmethod
    def calculate(area, cost_per_unit_area, yield_exp, price_exp):
        """
        Core Logic to calculate profit.:
        Profit = (Yield * Area * Price) - (Cost * Area)
        """
        try:
            if any(v < 0 for v in [area, cost_per_unit_area, yield_exp, price_exp]):
                raise ValueError("Negative inputs not allowed.")

            total_rev = area * yield_exp * price_exp
            total_cost = area * cost_per_unit_area
            net_profit = total_rev - total_cost

            return {
                "total_revenue": total_rev,
                "total_cost": total_cost,
                "net_profit": net_profit,
                "status": "Profit" if net_profit >= 0 else "Loss"
            }
        except Exception:
            return None