import sys
import requests
def main(hash):
    print('Weight 0-10, 4 takes the stone to the button.')
    print('Line 0-180, 0 is straight to the right, 90 is straight to house, 180 is straight to left.')
    print('Curl -10 - 10. -10 curls fiercely to right, 0 no curl, 10 curls fiercely to the left.')
    print("\n\n\n\n\n\n")
    print('Format <weightvalue>,<linevalue>,<curlvalue>')
    while(True):
        shizzle = input('Gimme input\n')
        shezmaz = shizzle.split(',')
        if len(shezmaz) < 3:
            print('Something went wrong with your input. Try again.')
        else:
            curl(shezmaz, hash)
            print('Your curl has been sent. Watch your rock and wait for the next turn.')
        
def curl(inputs, hash):
    url = 'https://curling.goforecrew.com/delivery'
    headers = {'Authorization': 'Bearer ' + hash, 'User-agent': 'curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.20051: 1.4 OpenSSL/0.9.8r zlib/1.2.5'}
    params = {'weight': int(inputs[0]), 'line': int(inputs[1]), 'curl': int(inputs[2])}
    print(params)
    r = requests.put(url, headers=headers, params=params)
    print(r.text)
    print(r.status_code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No hash inputted. Exiting.')
    main(sys.argv[1])
