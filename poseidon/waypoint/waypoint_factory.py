import logging
import ruamel.yaml
from poseidon.waypoint.waypoint import Waypoint
from poseidon.exception.settings_exception import SettingsException


def load_settings_waypoints(settings_location: str) -> list:
    with open(settings_location) as fp:
        data = ruamel.yaml.safe_load(fp)

        try:
            if data['waypoints']:
                return data['waypoints']
        except (KeyError, TypeError):
            raise SettingsException.for_missing_waypoints()


class WaypointFactory:

    # TODO: try & catch
    @staticmethod
    def create_waypoints(settings_location) -> list:
        created_waypoints = []

        logging.info('Loading all waypoints ...')
        for waypoint in load_settings_waypoints(settings_location):
            waypoint_coordinate_x = waypoint['x']
            waypoint_coordinate_y = waypoint['y']
            created_waypoints.append(Waypoint(waypoint_coordinate_x, waypoint_coordinate_y))

            logging.info('Detected waypoint %s %s', waypoint_coordinate_x, waypoint_coordinate_y)

        logging.info('Finished loading all waypoints.')
        return created_waypoints
