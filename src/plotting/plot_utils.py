import pandas as pd
from scipy.interpolate import interp1d


def interpolate(df, x='Time', y='Survival', kind='zero'):
    """Wrapper function for scipy.interpolate.interp1d.

    Args:
        df (pd.DataFrame): data to make interpolation.
        x (str, optional): column name to use as x values. Defaults to 'Time'.
        y (str, optional): column name to use as y values. Defaults to 'Survival'.
        kind (str, optional): Specifies the kind of interpolation. 
                              Feeds in to kind argument of interp1d function.. Defaults to 'zero'.

    Returns:
        _type_: _description_
    """    
    return interp1d(df[x], df[y], kind=kind, fill_value='extrapolate')

def import_input_data():
    """Import input data excluding supplementary combinations.

    Returns:
        (str, pd.DataFrame): a tuple of input directory path and input data
    """
    indir = '../data/PFS_predictions/'
    cox_df = pd.read_csv(indir + 'cox_ph_test.csv', index_col=False)
    # remove supplementary
    cox_df = cox_df[cox_df['Figure'] != 'suppl'].reset_index()
    return indir, cox_df


def import_input_data_include_suppl():
    """Import input data including supplementary combinations.

    Returns:
        (str, pd.DataFrame): a tuple of input directory path and input data
    """
    indir = '../data/PFS_predictions/'
    cox_df = pd.read_csv(indir + 'cox_ph_test.csv', index_col=False)
    return indir, cox_df


def set_figsize(scale, rows, cols, spacing_width_scale=0.2, spacing_height_scale=0.2):
    """Set figure size.

    Args:
        scale (float): scale
        rows (int): number of rows in a figure
        cols (int): number of columns in a figure

    Returns:
        (float, float): (width, height) of the figure
    """    
    subplot_abs_width = 2 * scale  # Both the width and height of each subplot
    # The width of the spacing between subplots
    subplot_abs_spacing_width = spacing_width_scale * scale
    # The height of the spacing between subplots
    subplot_abs_spacing_height = spacing_height_scale * scale
    # The width of the excess space on the left and right of the subplots
    subplot_abs_excess_width = 0.3 * scale
    # The height of the excess space on the top and bottom of the subplots
    subplot_abs_excess_height = 0.3 * scale

    fig_width = (cols * subplot_abs_width) + ((cols-1) *
                                              subplot_abs_spacing_width) + subplot_abs_excess_width
    fig_height = (rows * subplot_abs_width) + ((rows-1) * 
                                                subplot_abs_spacing_height) + subplot_abs_excess_height
    return (fig_width, fig_height)


def get_model_colors():
    """Returns preset colors for trial arms.

    Returns:
        dict: color dictionary
    """    
    # define colors
    blue = [i/255 for i in (0, 128, 255)]  # hsa
    red = [i/255 for i in (200, 0, 50)]  # additivity

    color_dict = {'HSA': blue, 'additive': red, 'control': 'orange', 'experimental': 'green', 'combo': 'black'}
    return color_dict