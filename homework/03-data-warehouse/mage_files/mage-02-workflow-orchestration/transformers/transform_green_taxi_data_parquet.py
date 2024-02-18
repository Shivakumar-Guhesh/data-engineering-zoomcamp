
import re

def toSnakeCase(string):
    string = re.sub(r'(?<=[a-z])(?=[A-Z])|[^a-zA-Z]', ' ', string).strip().replace(' ', '_')
    return ''.join(string.lower())

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # data = data.loc[(data['passenger_count']>0) & (data['trip_distance']>0) ]
    # print(f'Shape after removing rows with passenger_count<=0 or trip_distance <=0: {data.shape}')

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    old_columns = list(data.columns.values)
    # print('Before transforming')
    # print(columns)
    new_columns = [toSnakeCase(column) for column in old_columns]
    # print('After transforming')
    # print(columns)
    data.columns = new_columns
    print(f'Differences: {list(set(old_columns) - set(new_columns))}')
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # assert output['vendor_id'].isin(available_vendor_ids).all(), 'vendor_id is not one of the existing values in the column'
    # assert ((output['passenger_count'] > 0).all()), 'passenger_count <=0 exists'
    # assert ((output['trip_distance'] > 0).all()), 'trip_distance <=0 exists'

    # assert output.loc[output['passenger_count'] < 0].all(), 'passenger_count <=0 exists'
