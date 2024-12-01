import pyshark
import logging

def capture_traffic(interface, capture_duration):
    capture = None
    try:
        logging.info(f"Attempting to capture traffic on {interface} for {capture_duration} seconds...")
        # Initialize the capture object
        capture = pyshark.LiveCapture(interface=interface)
        capture.sniff(timeout=capture_duration)
        logging.info(f"Captured {len(capture)} packets.")
        return list(capture)
    except Exception as e:
        logging.error(f"Error during capture: {e}")
        return []
    finally:
        if capture:
            try:
                capture.close()
                logging.info("Capture process closed.")
            except Exception as e:
                logging.warning(f"Error closing capture: {e}")
