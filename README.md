Daniil Zakhlystov

**TCP port scanner**

Scans the provided tcp ports range of the provided target.

**Usage:**

usage: launch.py [-h] [-t T] host start end

positional arguments:

  host        target IP or domain name
  
  start       port scan start port
  
  end         port scan end port

optional arguments:

  -h, --help  show this help message and exit
  
  -t T        Option to specify tcp connection timeout (in seconds).


**Launch sample:**

python launch.py 8.8.8.8 22 53 -t 0.5
