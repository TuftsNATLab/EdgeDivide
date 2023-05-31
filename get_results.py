from ripe.atlas.cousteau import (
  Measurement,
  AtlasResultsRequest,
)
from ripe.atlas.sagan import (
  PingResult,
)

from multiprocessing import Pool

def getMeasurementResults(msm_id, kind=PingResult, **kwargs):
    args = { "msm_id": msm_id }
    args.update(kwargs)
    is_success, results = AtlasResultsRequest(**args).create()
    if is_success == False:
      raise "Request failed"
    measurement = Measurement(id=msm_id)
    results = list(map(lambda r: kind(r), results))
    return [measurement, results]

def getMeasurementsParallel(inputs):
  msm_id = inputs[0]
  kind = inputs[1]
  return getMeasurementResults(msm_id, kind)

def getMeasurementsResults(msm_ids, kind=PingResult):
  pool = Pool(5)
  return pool.map(getMeasurementsParallel, [[id, kind] for id in msm_ids])