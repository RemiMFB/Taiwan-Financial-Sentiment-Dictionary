#!/usr/bin/env python
import pandas as pd
from collections import Counter

def macro_f1(y_true, y_pred):
    labels = sorted(set(y_true) | set(y_pred))
    f1s = []
    for c in labels:
        tp = sum((yt==c and yp==c) for yt, yp in zip(y_true,y_pred))
        fp = sum((yt!=c and yp==c) for yt, yp in zip(y_true,y_pred))
        fn = sum((yt==c and yp!=c) for yt, yp in zip(y_true,y_pred))
        prec = tp / (tp+fp) if (tp+fp)>0 else 0.0
        rec = tp / (tp+fn) if (tp+fn)>0 else 0.0
        f1 = 2*prec*rec/(prec+rec) if (prec+rec)>0 else 0.0
        f1s.append(f1)
    return sum(f1s)/len(f1s) if f1s else 0.0

if __name__ == "__main__":
    df = pd.read_csv("data/validation_sample.csv")
    acc = (df["gold"]==df["pred"]).mean()
    f1 = macro_f1(df["gold"].tolist(), df["pred"].tolist())
    print(f"Accuracy: {acc:.3f}")
    print(f"Macro-F1: {f1:.3f}")
