-- Targeting SQLITE
-- Author: Benqing Shen
CREATE TABLE PredictedVolatility
(
  TimeSeriesId INTEGER,
  ModelId INTEGER,
  AsOfDate TEXT, -- TEXT OR INTEGER
  PredictHorizon INTEGER,
  PredictedVolatility REAL,
  PRIMARY KEY
  (
    TimeSeriesId,
    ModelId,
    AsOfDate,
    PredictHorizon
  )
);

-- Conform to Yahoo format
CREATE TABLE HistoricalQuotesOHLC
(
  Id INTEGER, -- Symbol Id. Any other good name?
  QuoteDate TEXT, -- TEXT OR INTEGER
  Open REAL,
  High REAL,
  Low REAL,
  Close REAL,
  Volume INTEGER, -- INTEGER OR REAL
  AdjClose REAL,
  PRIMARY KEY
  (
    Id,
    QuoteDate
  )
);