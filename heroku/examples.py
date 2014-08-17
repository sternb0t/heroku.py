# coding=utf-8
import os
import heroku
from pprint import pprint# noqa
#import socket

#import httplib
#import logging
#httplib.HTTPConnection.debuglevel = 1
#logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
#logging.getLogger().setLevel(logging.INFO)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.INFO)
#requests_log.propagate = True

HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY', False)
HEROKU_APPNAME = os.environ.get('HEROKU_APPNAME', False)
TEST_EMAIL = os.environ.get('TEST_EMAIL', False)

heroku_conn = heroku.from_key(HEROKU_API_KEY)

#app = heroku_conn.create_app(name='testy2124app', stack_id_or_name='cedar', region_id_or_name='us')
#print app.addons()
#print heroku_conn.addons('testy123app')
#for addon in app.addons():
    #addon.delete()

#del config['TEST1']
#del config['TEST2']
#del config['TEST3']
#del config['Z01']
#del config['Z02']
#print config
#config['TEST1'] = u'MM1'
#config['TEST2'] = u'MM2'
#config['TEST3'] = u'MM3'
#config2 = heroku_conn.update_appconfig('testy123app', {u'Z01': u'A1', u'Z02': u'A2'})
#config2 = config.update({u'Z01': u'A1', u'Z02': u'A2'})
#config3 = app.config()
#print config
#print "======"
#print config2
#print "======"
#print config3
#print config['TEST1']
#print config['TEST3']

#app = heroku_conn.app('kdsjhkszdjhgksjdhfkj')
#procs = app.process_formation()
#proc = app.process_formation()['web']
#print proc.size
#print proc.quantity
#print procs
#proc.scale(0)
#app.scale_formation_process('web', 1)
#output = app.run_command('pgbackups:url')
#collab = app.add_collaborator(email=TEST_EMAIL, silent=False)
#collab = app.remove_collaborator(TEST_EMAIL)
#print newapp.collaborators()
#config = newapp.config()
#config['TEST2'] = None
#print newapp.domains()

#domain2 = newapp.add_domain('testy123.testing.com')
#print newapp.domains()
#newapp.remove_domain('testy123.testing.com')
#domain.remove()
#print newapp.domains()

#app = heroku_conn.app(HEROKU_APPNAME)
#pprint(app.addons())
#dynos = app.dynos()

#dyno = dynos['web.1']
#print dyno
#releases = app.releases(sort='asc')
#for release in releases:
    #print "{0} {1} {2} {3}".format(release.id, release.commit, release.user, release.description)
#releases = app.releases()._items.reverse()
#print releases.pop()
#print releases.pop()

#app.rollback('v108')


#apps = heroku_conn.apps(order_by='name')

#for app in apps:
    #print app.name

#app.rename('testy223')

#print app.enable_maintence_mode()
#print app.disable_maintence_mode()
#app.enable_feature('user-env-compile')
#app.disable_feature('user-env-compile')
#print app.labs()
#print heroku_conn.features()
#domain = app.add_domain('test123-1.testing.com')
#domain = app.add_domain('test123-2.testing.com')
#domain = app.add_domain('test123-3.testing.com')
#domain = app.add_domain('test123-4.testing.com')
#domain = app.add_domain('test123-5.testing.com')
#domain = app.add_domain('test123-6.testing.com')
#domain = app.add_domain('test123-7.testing.com')

#iterator = app.stream_log(lines=1)
#for line in iterator:

    # filter out keep-alive new lines
    #if line:
        #print "{0}".format(line)

#logs = app.get_log(lines=100)
#print logs

#print app.domains(limit=1)
#dyno = app.run_command('fab -l', printout=True)
#dyno.remove()
#proc = heroku_conn.apps()['testy123app'].process_formation()['web']
#print proc.size
#print proc.quantity

#formations = app.process_formation()
#print formations['web']
#for formation in formations:
    #formation.resize(1)
    #print app._h._last_request_id

#print app.dynos()['web.1']
#print dynos['web.1']

#print heroku_conn.apps()['testy123app']
#print heroku_conn.apps()['d32b74d8-f5cf-4e3e-95dd-a601668fdb0c']
#for dyno in app.dynos():
    #print dyno
    #print dyno.command
    #dyno.restart()

#app.restart()
#del config['TEST2']

#newapp.remove_collaborator('testing125146513@mail.com')
#collab.remove()
#pprint(newapp.addons)
#app = heroku_conn.app('testy123app')
#for addon in app.addons:
    #print addon.app.name, " - ", addon.plan.name

#addons = heroku_conn.addon_services()
#pprint(addons)

#pg_addon = heroku_conn.addon_services('6235c964-8b3c-47e0-952f-8d8f6a2d53f5')
#pg_addon = heroku_conn.addon_services(id_or_name='heroku-postgresql')
#pprint(pg_addon)


#for addon in addons:
    #print addon.name, " - ", addon.id, " - ", addon.id, " - ", addon.price
    #addon.upgrade(plan_id_or_name='heroku-postgresql:basic')
    #addon.delete()

#app.delete()

print heroku_conn._last_request_id

# -----------------
# pgbackup examples
# -----------------
#
# pgb_client = heroku.pg_backups(os.getenv("PGBACKUPS_URL"))
# print pgb_client

# # most recent backup
# latest = pgb_client.latest_backup()
# pprint([latest.id, latest.name, latest.from_name, latest.created_at, latest.public_url])

# # list backups
# backups = pgb_client.backups()
# for backup in backups:
#     print backup
#
# # get backup by name
# backups = pgb_client.backups()
# one_backup = backups[0]
# backup = pgb_client.backup(one_backup.name)
# pprint(backup)
#
# # list transfers - similar to backups, but no public url
# transfers = pgb_client.transfers(order_by='created_at')
# transfer = transfers[0]
# pprint(transfer.dict())

# # create capture, i.e. back up the database to s3 - only run once!
# if os.environ.get('DATABASE_URL'):
#     transfer = pgb_client.capture(os.environ.get('DATABASE_URL'), 'DATABASE_URL')
#     pprint(transfer)
#     pprint(transfer.dict())

# # poll for transfer completion
# import time
# transfer = pgb_client.transfer(21308792)
# while transfer.progress != "upload done":
#     time.sleep(10)
#     transfer = pgb_client.transfer(21308792)
#     print "Transfer: {}, {}, {}s".format(transfer.progress, transfer.size, transfer.duration)
# pprint(transfer.dict())

# # get the public url of a capture transfer - use transfer.name -> backup.name
# pprint(pgb_client.backup(transfer.name).public_url)

# # destroy (aka delete) a backup - warning, this is permanent
# pgb_client.destroy(pgb_client.latest_backup().name)
# pgb_client.delete(pgb_client.latest_backup().name)

# -----------------
# postgres examples
# -----------------
#
# hpg = heroku.postgres(HEROKU_API_KEY)
# print hpg

# # get default db (DATABASE_URL)
# pprint(hpg.database("myapp-dev"))
# # get db via full attachment name
# pprint(hpg.database("myapp-dev", "HEROKU_POSTGRESQL_PURPLE_URL"))
# # via short attachment name
# pprint(hpg.database("myapp-prod", "PURPLE"))

# # get db info list
# pprint(hpg.database("myapp-dev").info)

# # get db metrics
# pprint(hpg.database("myapp-dev").metrics())

# # poll for waiting status (like after upgrade or attach)
# import time
# while hpg.database("myapp-dev").is_waiting:
#     time.sleep(10)

# # get db maintenance info - does it need maintenance?
# pprint(hpg.database("myapp-dev").maintenance().message)

# # reset a db - warning, this is permanent
# db = hpg.database("myapp-dev")
# db.reset()

# # get running processes
# pprint(hpg.database("myapp-dev").ps())

# # exec ad-hoc sql
# pprint(hpg.database("myapp-dev").exec_sql("select * from table limit 10;"))
