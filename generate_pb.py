import time
from google.transit import gtfs_realtime_pb2

# Crear el mensaje GTFS-Realtime
feed = gtfs_realtime_pb2.FeedMessage()

# Encabezado
feed.header.gtfs_realtime_version = "2.0"
feed.header.incrementality = gtfs_realtime_pb2.FeedHeader.FULL_DATASET
feed.header.timestamp = 1656230726  # Puedes usar int(time.time()) si quieres el tiempo actual

# Entidad con TripUpdate
entity = feed.entity.add()
entity.id = "1"
trip_update = entity.trip_update
trip_update.trip.trip_id = "TRIP1"
trip_update.trip.route_id = "ROUTE1"
trip_update.trip.start_time = "10:00:00"
trip_update.trip.schedule_relationship = gtfs_realtime_pb2.TripDescriptor.SCHEDULED

# StopTimeUpdate
stop_time_update = trip_update.stop_time_update.add()
stop_time_update.stop_sequence = 1
stop_time_update.stop_id = "PARADA1"
stop_time_update.arrival.delay = 120

# Guardar como archivo .pb
with open("basicFeed.pb", "wb") as f:
    f.write(feed.SerializeToString())

print("Archivo basicFeed.pb generado correctamente.")
