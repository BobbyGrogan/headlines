option_o=false
extra_args=() # Initialize an array to hold extra arguments

while getopts "fiseychow" opt; do
  case $opt in
    h)
      cat << EOF
-c (Congressional Reports)
-y (Y-Combinator Hacker News)
-e (Economist Headlines)
-i (Infosec Magazine)
-f (Financial Times Market News)
-s (Stratfor Geopolitics)
-w (Wikipedia Current Events)

-wo, -so, etc. (Open that site)
EOF
      ;;
    c)
      command="/home/rex/code/headlines/congressionalreports.sh"
      ;;
    y)
      command="/home/rex/code/headlines/ycombnews.sh"
      ;;
    e)
      command="/home/rex/code/headlines/economist.sh"
      ;;
    f)
      command="/home/rex/code/headlines/ftmarkets.sh"
      ;;
    i)
      command="/home/rex/code/headlines/infosecuritymag.sh"
      ;;
    s)
      command="/home/rex/code/headlines/stratfor.sh"
      ;;
    w)
      command="/home/rex/code/headlines/wikinews.sh"
      ;;
    o)
      option_o=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Shift getopts processed options out of the way
shift $((OPTIND-1))

# Any remaining arguments are captured as extra arguments
extra_args+=("$@")

# Check if -o was set and modify the command accordingly
if $option_o; then
  command="$command -o"
fi

# Pass along any extra arguments to the command
if [ -n "$command" ]; then
  if [ ${#extra_args[@]} -eq 0 ]; then
    eval $command
  else
    eval $command "${extra_args[@]}"
  fi
else
  echo ""
fi
