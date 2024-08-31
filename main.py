from init_config import STATE
from ui_flow import lcd_logger


def main():
    from udp_server import UDP_Server
    lcd_logger.info("Uruchamianie serwera UDP")
    udp_server = UDP_Server(STATE, lcd_logger)
    udp_server.spin_udp_server()


main()
