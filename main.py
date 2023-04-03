"""
main
"""

def run_bot()->None:
    """run_bot"""
    while True:
        inp:str = input("#")

def main()->None:
    """main"""
    print("hello")
    try:
        run_bot()
    except KeyboardInterrupt:
        print("bye")

if __name__ == "__main__":
    main()