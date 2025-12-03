import argparse

from app_name.main import main


def _enable_debug_mode():
    import debugpy

    if not debugpy.is_client_connected():
        debugpy.listen(5678)
        print("*** Waiting for client to attach on port 5678... ***")
        debugpy.wait_for_client()
    print("*** Debugger attached successfully! Continuing execution. ***")
    debugpy.breakpoint()


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Run the application in debug mode, and wait for debugger to attach."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_arguments()
    if args.debug:
        _enable_debug_mode()
    main()
