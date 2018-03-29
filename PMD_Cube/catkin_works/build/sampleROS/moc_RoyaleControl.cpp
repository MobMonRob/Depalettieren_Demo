/****************************************************************************
** Meta object code from reading C++ file 'RoyaleControl.hpp'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../src/sampleROS/inc/RoyaleControl.hpp"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'RoyaleControl.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_royale_in_ros__RoyaleControl[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      10,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      42,   30,   29,   29, 0x08,
      68,   62,   29,   29, 0x08,
     101,   89,   29,   29, 0x08,
     123,   62,   29,   29, 0x08,
     141,   62,   29,   29, 0x08,
     159,   62,   29,   29, 0x08,
     175,   29,   29,   29, 0x08,
     204,   29,   29,   29, 0x08,
     230,   29,   29,   29, 0x08,
     256,   29,   29,   29, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_royale_in_ros__RoyaleControl[] = {
    "royale_in_ros::RoyaleControl\0\0currentMode\0"
    "setUseCase(QString)\0value\0"
    "setExposureTime(int)\0isAutomatic\0"
    "setExposureMode(bool)\0setMinFilter(int)\0"
    "setMaxFilter(int)\0setDivisor(int)\0"
    "preciseExposureTimeSetting()\0"
    "preciseMinFilterSetting()\0"
    "preciseMaxFilterSetting()\0"
    "preciseDivisorSetting()\0"
};

void royale_in_ros::RoyaleControl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        RoyaleControl *_t = static_cast<RoyaleControl *>(_o);
        switch (_id) {
        case 0: _t->setUseCase((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->setExposureTime((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->setExposureMode((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->setMinFilter((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->setMaxFilter((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->setDivisor((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->preciseExposureTimeSetting(); break;
        case 7: _t->preciseMinFilterSetting(); break;
        case 8: _t->preciseMaxFilterSetting(); break;
        case 9: _t->preciseDivisorSetting(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData royale_in_ros::RoyaleControl::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject royale_in_ros::RoyaleControl::staticMetaObject = {
    { &rviz::Panel::staticMetaObject, qt_meta_stringdata_royale_in_ros__RoyaleControl,
      qt_meta_data_royale_in_ros__RoyaleControl, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &royale_in_ros::RoyaleControl::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *royale_in_ros::RoyaleControl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *royale_in_ros::RoyaleControl::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_royale_in_ros__RoyaleControl))
        return static_cast<void*>(const_cast< RoyaleControl*>(this));
    typedef rviz::Panel QMocSuperClass;
    return QMocSuperClass::qt_metacast(_clname);
}

int royale_in_ros::RoyaleControl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    typedef rviz::Panel QMocSuperClass;
    _id = QMocSuperClass::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 10)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 10;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
