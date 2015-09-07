# NOTICE:
#
# Application name defined in TARGET has a corresponding QML filename.
# If name defined in TARGET is changed, the following needs to be done
# to match new name:
#   - corresponding QML filename must be changed
#   - desktop icon filename must be changed
#   - desktop filename must be changed
#   - icon definition filename in desktop file must be changed
#   - translation filenames have to be changed

# The name of your application
TARGET = sailfishos-patch-restore-swipe-to-lock

TEMPLATE = aux

patch.path = /usr/share/patchmanager/patches/eugenio-restore-swipe-to-lock
patch.files = data/unified_diff.patch data/patch.json

INSTALLS += \
	patch


OTHER_FILES += \
    rpm/sailfishos-patch-restore-swipe-to-lock.changes.in \
    rpm/sailfishos-patch-restore-swipe-to-lock.spec \
    rpm/sailfishos-patch-restore-swipe-to-lock.yaml \
    data/unified_diff.patch \
    data/patch.json
