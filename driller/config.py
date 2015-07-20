### Redis Options
REDIS_HOST="localhost"
REDIS_PORT=6379
REDIS_DB=1

### Celery Options
BROKER_URL="amqp://guest@localhost//"

### Environment Options

# directory contain driller-qemu versions, relative to the directoy node.py is invoked in
QEMU_DIR="driller-qemu"

# directory containing the binaries, used by the driller node to find binaries
BINARY_DIR="/cgc/binaries/"

### Fuzzer options

# how often to check for crashes in seconds
CRASH_CHECK_INTERVAL=60

# how long to fuzz before giving up in seconds
FUZZ_TIMEOUT=60 * 60 * 24
