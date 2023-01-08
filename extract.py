from os.path import join


def extract_tbl(tbl_name, curs, des: str):
    for tbl in tbl_name:
        curs.execute("SELECT * from {}".format(tbl))
        pd_df = curs.fetch_pandas_all()
        if pd_df.to_csv(path_or_buf=join(des, "{}.csv".format(tbl)),
                        index=False, header=False) is None:
            print("Wrote to file {}.csv".format(join(des, tbl)))
