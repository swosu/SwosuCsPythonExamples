import user_interactions as ui




if __name__ == "__main__":
    city_count = ui.ask_how_many_cities()
    ui.respond_to_user_city_count(city_count)