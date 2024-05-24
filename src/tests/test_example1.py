from pathlib import Path
import os
import pytest

# extend path for imports
filepath = Path(__file__).parents[1]
os.sys.path.append(str(filepath))
from example1 import CerealAnalysis  # noqa


@pytest.fixture
def ca():
    file_path = Path(__file__).parents[2]
    data_path = file_path / "data" / "cereal.csv"
    ca = CerealAnalysis(data_path)
    return ca


def test_cerealanalysis(ca):
    assert ca.n_rows == 77
    assert ca.n_cols == 16
    assert ca.columns.tolist() == [
        "name",
        "mfr",
        "type",
        "calories",
        "protein",
        "fat",
        "sodium",
        "fiber",
        "carbo",
        "sugars",
        "potass",
        "vitamins",
        "shelf",
        "weight",
        "cups",
        "rating",
    ]
    assert ca.numeric_cols.tolist() == [
        "calories",
        "protein",
        "fat",
        "sodium",
        "fiber",
        "carbo",
        "sugars",
        "potass",
        "vitamins",
        "shelf",
        "weight",
        "cups",
        "rating",
    ]
    assert ca.categorical_cols.tolist() == ["name", "mfr", "type"]
    assert ca.missing_values.sum() == 0
    assert ca.unique_values["name"] == 77
    assert ca.dtypes["name"] == "object"


def test_get_numeric_summary(ca):
    numeric_summary = ca.get_numeric_summary()
    assert numeric_summary["calories"]["mean"] == pytest.approx(106.88311, 0.00001)
    assert numeric_summary["protein"]["mean"] == 2.5454545454545454
    assert numeric_summary["fat"]["mean"] == 1.012987012987013
    assert numeric_summary["sodium"]["mean"] == 159.67532467532467
    assert numeric_summary["fiber"]["mean"] == 2.1519480519480516
    assert numeric_summary["carbo"]["mean"] == 14.597402597402597
    assert numeric_summary["sugars"]["mean"] == 6.922077922077922
    assert numeric_summary["potass"]["mean"] == 96.07792207792207
    assert numeric_summary["vitamins"]["mean"] == 28.246753246753247
    assert numeric_summary["shelf"]["mean"] == 2.207792207792208
    assert numeric_summary["weight"]["mean"] == 1.0296103896103896
    assert numeric_summary["cups"]["mean"] == 0.821038961038961
    assert numeric_summary["rating"]["mean"] == 42.66570498701299


def test_get_missing_values(ca):
    missing_values = ca.get_missing_values()
    assert missing_values.sum() == 0
