import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^([0-9]{1,2}(?::[0-9]{1,2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{1,2})?) (AM|PM)$",
        s,
        re.IGNORECASE,
    ):
        fir_hr, ampm_1, sec_hr, ampm_2 = (
            matches.group(1),
            matches.group(2),
            matches.group(3),
            matches.group(4),
        )
        fir_mi, sec_mi = 0, 0
        if ":" in fir_hr:
            fir_hr, fir_mi = fir_hr.split(":")
            if int(fir_mi) >= 60:
                raise ValueError()
        if ":" in sec_hr:
            sec_hr, sec_mi = sec_hr.split(":")
            if int(sec_mi) >= 60:
                raise ValueError()
        if fir_hr == "12" and ampm_1 == "AM":
            fir_hr = 0
        elif int(fir_hr) != 12 and ampm_1 == "PM":
            fir_hr = int(fir_hr) + 12
        if sec_hr == "12" and ampm_2 == "AM":
            sec_hr = 0
        elif int(sec_hr) != 12 and ampm_2 == "PM":
            sec_hr = int(sec_hr) + 12
        fir_hr, fir_mi, sec_hr, sec_mi = (
            str(fir_hr).zfill(2),
            str(fir_mi).zfill(2),
            str(sec_hr).zfill(2),
            str(sec_mi).zfill(2),
        )
        return f"{fir_hr}:{fir_mi} to {sec_hr}:{sec_mi}"
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
