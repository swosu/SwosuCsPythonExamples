import user_interactions as ui
import distance_table_handler as dth

import spp_guess_and_check as gc




if __name__ == "__main__":

    # priliminary user interactions
    city_count = ui.ask_how_many_cities()
    ui.respond_to_user_city_count(city_count)
    run_time = ui.ask_how_long_to_run()
    distance_table = []
    # initilize distance table
    distance_table = [[0 for i in range(cols)] for j in range(rows)]
    distance_table = dth.load_distance_table(city_count, distance_table)
    print('distance table right after the load call in main: ')
    print(distance_table)
    ui.respond_to_user_run_time(run_time)

    # run guess and check
    gc.run_guess_and_check(city_count, run_time, distance_table)

    

