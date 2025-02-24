
from typing import Text, List

# At least one feature is needed.


# Name of features which have continuous float values. These features will be
# used as their own values.
DENSE_FLOAT_FEATURE_KEYS = ['weathersit', 'temp', 'atemp', 'hum', 'windspeed']

# Name of features which have continuous float values. These features will be
# bucketized using `tft.bucketize`, and will be used as categorical features.
# BUCKET_FEATURE_KEYS = ['pickup_latitude']
# Number of buckets used by tf.transform for encoding each feature. The length
# of this list should be the same with BUCKET_FEATURE_KEYS.
# BUCKET_FEATURE_BUCKET_COUNT = [10]

# Name of features which have categorical values which are mapped to integers.
# These features will be used as categorical features.
CATEGORICAL_FEATURE_KEYS = [ 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday']
# Number of buckets to use integer numbers as categorical features. The length
# of this list should be the same with CATEGORICAL_FEATURE_KEYS.
CATEGORICAL_FEATURE_MAX_VALUES = [4, 4, 12, 24, 2, 5, 2]

# Name of features which have string values and are mapped to integers.
VOCAB_FEATURE_KEYS = []

# Uncomment below to add more features to the model
# DENSE_FLOAT_FEATURE_KEYS = ['trip_miles', 'fare', 'trip_seconds']
#
# BUCKET_FEATURE_KEYS = [
#     'pickup_latitude', 'pickup_longitude', 'dropoff_latitude',
#     'dropoff_longitude'
# ]
# # Number of buckets used by tf.transform for encoding each feature.
# BUCKET_FEATURE_BUCKET_COUNT = [10, 10, 10, 10]
#
# CATEGORICAL_FEATURE_KEYS = [
#     'trip_start_hour', 'trip_start_day', 'trip_start_month'
# ]
# # Number of buckets to use integer numbers as categorical features.
# CATEGORICAL_FEATURE_MAX_VALUES = [24, 31, 12]
#
#
# VOCAB_FEATURE_KEYS = [
#     'payment_type',
#     'company',
# ]

# Number of vocabulary terms used for encoding VOCAB_FEATURES by tf.transform
VOCAB_SIZE = 1000

# Count of out-of-vocab buckets in which unrecognized VOCAB_FEATURES are hashed.
OOV_SIZE = 10

# Keys
LABEL_KEY = 'cnt'
FARE_KEY = 'fare'


def transformed_name(key: Text) -> Text:
  """Generate the name of the transformed feature from original name."""
  return key + '_xf'


def vocabulary_name(key: Text) -> Text:
  """Generate the name of the vocabulary feature from original name."""
  return key + '_vocab'


def transformed_names(keys: List[Text]) -> List[Text]:
  """Transform multiple feature names at once."""
  return [transformed_name(key) for key in keys]
