import cProfile
import example
import os
import pstats
import pandas as pd

def profile_to_csv(stats_file, output_csv):
    stats = pstats.Stats(stats_file)
    stats_list = []

    for function_info, (ccalls, ncalls, tt, ct, callers) in stats.stats.items():
        stats_list.append({
            "filename": function_info[0],
            "lineno": function_info[1],
            "function": function_info[2],
            "ncalls": ncalls,
            "tottime": tt,
            "cumtime": ct,
        })

    df = pd.DataFrame(stats_list)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    profile_output = "example_profile.bin"
    cProfile.run("example.main()", profile_output)

    # 将 cProfile 结果转换为 CSV 文件
    profile_to_csv(profile_output, "example_profile.csv")

    # 使用 snakeviz 可视化 cProfile 结果
    os.system(f"snakeviz {profile_output}")