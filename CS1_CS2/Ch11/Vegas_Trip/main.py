import input_module
import calculations
import summary
import printer


def main():
    print("Welcome to the Las Vegas Trip Planner")
    trip_data = input_module.collect_trip_details()
    cost_data = calculations.calculate_trip_costs(trip_data)
    trip_summary = summary.summarize_trip(trip_data, cost_data)
    printer.print_results(trip_summary)

if __name__ == "__main__":
    main()