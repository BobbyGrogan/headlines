option_o=false

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

# Check if -o was set and modify the command accordingly
if $option_o; then
  command="$command -o"
fi

# Execute the command
if [ -n "$command" ]; then
  eval $command
else
  echo ""
fi
