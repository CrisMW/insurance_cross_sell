def simplify_ax(*axs):
    """ Removes spines and removes ticks.
    Args:
        ax (matplotlib.axes.Axes): Axes object to simplify.
    Returns:
        ax (matplotlib.axes.Axes): Simplified Axes object.
    """
    for ax in axs:
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)    
        ax.spines["bottom"].set_visible(False)
        ax.tick_params(bottom=False, top=False, left=False, right=False)
        ax.grid(False)
        return ax

def rotate_ticks(ax):
    """ Rotates all ticks to 0 degrees
    Args:
        ax (matplotlib.axes.Axes): Axes with ticks to rotate.
    Returns:
        ax (matplotlib.axes.Axes): Adjusted Axes.
    """
    for tick in ax.get_xticklabels():
        tick.set_rotation(0)
    return ax
