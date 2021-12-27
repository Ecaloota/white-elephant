from numpy import printoptions
from simulator import generate_statistics
from parser import user_args
from writer import write_outputs
from plotter import write_plots

args = user_args()

steals, gifts, values, norm_values = generate_statistics(
    args.players, args.rounds, args.verbose, args.unbiased
)

if args.write in ["True", "true", "yes", "y"] or args.write is True:
    write_outputs(args.players, args.rounds, steals, gifts, values)

if args.plot in ["True", "true", "yes", "y"] or args.plot is True:
    write_plots(
        steals, gifts, norm_values
    )  ## TODO not normalised by number of times its generated!


print("-" * 30)
print(f"WHITE-ELEPHANT SIMULATOR")
print("-" * 30)
print(
    f"Data generated for {args.players} Players (biased: {args.unbiased}) over {args.rounds} iterations"
)
print(" ")
