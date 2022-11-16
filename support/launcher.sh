worker=$1
config=$2
id=$(aws ec2 request-spot-fleet --spot-fleet-request-config file://$config --query 'SpotFleetRequestId' --output text)
echo $id
if [[ $? -eq 0 ]]
then
  state=$(aws ec2 describe-spot-fleet-requests --spot-fleet-request-ids $id --query 'SpotFleetRequestConfigs[].SpotFleetRequestState' --output text)
  while [[ "$state" != "active" ]]
  do
    sleep 10
    state=$(aws ec2 describe-spot-fleet-requests --spot-fleet-request-ids $id --query 'SpotFleetRequestConfigs[].SpotFleetRequestState' --output text)
  done
  current_year=$(date +'%Y')
  current_day=$(date +'%d')
  current_month=$(date +'%m')
  current_hour=$(date +'%H')
  current_minute=$(date +'%M')
  sleep 10
  python3 launcher.py $worker $id $current_year $current_month $current_day $current_hour $current_minute
else
  echo "invalid json"
fi
#sfr-1e9b7c02-1c60-448a-8f61-bc6683ae6adc