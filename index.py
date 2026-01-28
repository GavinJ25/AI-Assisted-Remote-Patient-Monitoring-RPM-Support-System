import React, { useState, useEffect } from 'react';
import { Heart, Activity, AlertTriangle, Bell, Search, User, Users, Stethoscope, TrendingUp, TrendingDown, Thermometer, Droplet, Wind, Calendar, Clock, MapPin, Phone, ChevronRight, Zap, Check, X } from 'lucide-react';

const EnhancedDashboard = () => {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [selectedView, setSelectedView] = useState('overview');
  const [userRole, setUserRole] = useState('doctor');

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  // Sample data with more details
  const patients = [
    { 
      id: 1, 
      name: 'John Doe', 
      age: 65, 
      condition: 'Hypertension', 
      riskScore: 9.2, 
      status: 'critical', 
      hr: 125, 
      bp: '180/110', 
      spo2: 89,
      temp: 37.8,
      location: '123 Main St, Boston',
      lastUpdate: '2 min ago',
      trend: 'worsening',
      ambulanceETA: 4,
      deviceBattery: 45
    },
    { 
      id: 2, 
      name: 'Jane Smith', 
      age: 58, 
      condition: 'Diabetes', 
      riskScore: 7.8, 
      status: 'high', 
      hr: 98, 
      bp: '145/95', 
      spo2: 94,
      temp: 36.9,
      location: '456 Oak Ave, Boston',
      lastUpdate: '5 min ago',
      trend: 'stable',
      deviceBattery: 78
    },
    { 
      id: 3, 
      name: 'Robert Johnson', 
      age: 72, 
      condition: 'COPD', 
      riskScore: 5.2, 
      status: 'moderate', 
      hr: 88, 
      bp: '135/85', 
      spo2: 92,
      temp: 36.5,
      location: '789 Pine Rd, Boston',
      lastUpdate: '12 min ago',
      trend: 'improving',
      deviceBattery: 92
    },
    { 
      id: 4, 
      name: 'Emily Brown', 
      age: 45, 
      condition: 'Asthma', 
      riskScore: 2.1, 
      status: 'stable', 
      hr: 75, 
      bp: '120/80', 
      spo2: 98,
      temp: 36.6,
      location: '321 Elm St, Boston',
      lastUpdate: '8 min ago',
      trend: 'stable',
      deviceBattery: 88
    },
  ];

  const [selectedPatient, setSelectedPatient] = useState(patients[0]);

  const alerts = [
    { id: 1, type: 'critical', patient: 'John Doe', message: 'Emergency score 9.2! Ambulance dispatched - ETA 4 minutes', time: '2 min ago', action: 'dispatched' },
    { id: 2, type: 'high', patient: 'Jane Smith', message: 'Blood pressure elevated for 3 hours - Doctor notified', time: '15 min ago', action: 'notified' },
    { id: 3, type: 'moderate', patient: 'Robert Johnson', message: 'SpO2 trending downward - Continue monitoring', time: '45 min ago', action: 'monitoring' },
  ];

  const stats = [
    { label: 'Total Patients', value: '156', change: '+12', icon: Users, color: 'bg-blue-500' },
    { label: 'Critical Alerts', value: '3', change: '+1', icon: AlertTriangle, color: 'bg-red-500' },
    { label: 'Avg Response Time', value: '2.3m', change: '-0.5m', icon: Clock, color: 'bg-green-500' },
    { label: 'System Uptime', value: '99.9%', change: '+0.1%', icon: Zap, color: 'bg-purple-500' },
  ];

  const getStatusColor = (status) => {
    const colors = {
      critical: 'bg-red-100 text-red-800 border-red-300',
      high: 'bg-orange-100 text-orange-800 border-orange-300',
      moderate: 'bg-yellow-100 text-yellow-800 border-yellow-300',
      stable: 'bg-green-100 text-green-800 border-green-300'
    };
    return colors[status] || 'bg-gray-100 text-gray-800';
  };

  const getTrendIcon = (trend) => {
    if (trend === 'worsening') return <TrendingDown className="w-4 h-4 text-red-600" />;
    if (trend === 'improving') return <TrendingUp className="w-4 h-4 text-green-600" />;
    return <Activity className="w-4 h-4 text-gray-600" />;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50">
      {/* Top Navigation Bar */}
      <div className="bg-gradient-to-r from-indigo-600 to-blue-600 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-4">
              <div className="bg-white p-2 rounded-lg shadow-md">
                <Activity className="w-8 h-8 text-indigo-600" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-white">RemoteHealth AI</h1>
                <p className="text-indigo-100 text-sm">Intelligent Patient Monitoring</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-6">
              {/* Current Time */}
              <div className="text-white text-right">
                <div className="text-sm text-indigo-100">
                  {currentTime.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' })}
                </div>
                <div className="text-lg font-semibold">
                  {currentTime.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}
                </div>
              </div>

              {/* Role Selector */}
              <div className="flex items-center space-x-2 bg-white/10 backdrop-blur-sm px-4 py-2 rounded-lg">
                <Stethoscope className="w-5 h-5 text-white" />
                <select 
                  value={userRole} 
                  onChange={(e) => setUserRole(e.target.value)}
                  className="bg-transparent border-none outline-none font-medium text-white cursor-pointer"
                >
                  <option value="doctor" className="text-gray-800">Dr. Sarah Johnson</option>
                  <option value="nurse" className="text-gray-800">Nurse Station</option>
                  <option value="family" className="text-gray-800">Family View</option>
                </select>
              </div>

              {/* Notifications */}
              <div className="relative">
                <button className="bg-white/10 backdrop-blur-sm p-3 rounded-lg hover:bg-white/20 transition">
                  <Bell className="w-6 h-6 text-white" />
                  <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center font-bold">
                    {alerts.length}
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Stats Overview */}
      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
          {stats.map((stat, index) => (
            <div key={index} className="bg-white rounded-xl shadow-md p-5 border border-gray-100 hover:shadow-lg transition">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm font-medium">{stat.label}</p>
                  <p className="text-3xl font-bold text-gray-800 mt-1">{stat.value}</p>
                  <p className={`text-sm mt-1 ${stat.change.startsWith('+') ? 'text-green-600' : 'text-red-600'}`}>
                    {stat.change} from yesterday
                  </p>
                </div>
                <div className={`${stat.color} p-4 rounded-xl`}>
                  <stat.icon className="w-8 h-8 text-white" />
                </div>
              </div>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Patient List */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-xl shadow-lg border border-gray-100">
              <div className="p-5 border-b border-gray-100">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-xl font-bold text-gray-800">Active Patients</h2>
                  <span className="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm font-semibold">
                    {patients.length}
                  </span>
                </div>

                <div className="relative">
                  <Search className="absolute left-3 top-3 w-5 h-5 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search patients..."
                    className="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  />
                </div>
              </div>

              <div className="overflow-y-auto max-h-[600px]">
                {patients.map(patient => (
                  <div
                    key={patient.id}
                    onClick={() => setSelectedPatient(patient)}
                    className={`p-4 border-b border-gray-100 cursor-pointer transition-all ${
                      selectedPatient?.id === patient.id 
                        ? 'bg-indigo-50 border-l-4 border-l-indigo-500' 
                        : 'hover:bg-gray-50'
                    }`}
                  >
                    <div className="flex justify-between items-start mb-2">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2">
                          <h3 className="font-semibold text-gray-800">{patient.name}</h3>
                          {getTrendIcon(patient.trend)}
                        </div>
                        <p className="text-sm text-gray-600">{patient.age} yrs • {patient.condition}</p>
                      </div>
                      <span className={`px-3 py-1 rounded-full text-xs font-semibold border ${getStatusColor(patient.status)}`}>
                        {patient.status.toUpperCase()}
                      </span>
                    </div>
                    
                    <div className="flex items-center justify-between mt-3">
                      <div className="flex items-center space-x-3 text-sm">
                        <div className="flex items-center space-x-1">
                          <Heart className="w-4 h-4 text-red-500" />
                          <span className="font-medium">{patient.hr}</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <Activity className="w-4 h-4 text-blue-500" />
                          <span className="font-medium">{patient.bp}</span>
                        </div>
                        <div className="flex items-center space-x-1">
                          <Wind className="w-4 h-4 text-green-500" />
                          <span className="font-medium">{patient.spo2}%</span>
                        </div>
                      </div>
                      <div className={`text-xs font-semibold px-2 py-1 rounded ${
                        patient.riskScore >= 9 ? 'bg-red-100 text-red-700' :
                        patient.riskScore >= 7 ? 'bg-orange-100 text-orange-700' :
                        patient.riskScore >= 4 ? 'bg-yellow-100 text-yellow-700' :
                        'bg-green-100 text-green-700'
                      }`}>
                        {patient.riskScore}
                      </div>
                    </div>

                    {patient.status === 'critical' && (
                      <div className="mt-3 bg-red-50 border border-red-200 rounded-lg p-2 flex items-center space-x-2">
                        <Zap className="w-4 h-4 text-red-600" />
                        <span className="text-xs text-red-700 font-medium">Ambulance ETA: {patient.ambulanceETA} min</span>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Main Content Area */}
          <div className="lg:col-span-2 space-y-6">
            {/* Critical Alerts Banner */}
            {alerts.filter(a => a.type === 'critical').length > 0 && (
              <div className="bg-gradient-to-r from-red-500 to-red-600 rounded-xl shadow-lg p-6 text-white">
                <div className="flex items-start space-x-4">
                  <div className="bg-white/20 p-3 rounded-lg">
                    <AlertTriangle className="w-8 h-8" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-xl font-bold mb-2">CRITICAL EMERGENCY ACTIVE</h3>
                    <p className="text-red-50">{alerts[0].message}</p>
                    <div className="mt-4 flex items-center space-x-3">
                      <button className="bg-white text-red-600 px-4 py-2 rounded-lg font-semibold hover:bg-red-50 transition">
                        View Details
                      </button>
                      <button className="bg-white/20 text-white px-4 py-2 rounded-lg font-semibold hover:bg-white/30 transition">
                        Contact EMS
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Patient Details Card */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-100">
              <div className="bg-gradient-to-r from-indigo-500 to-blue-500 p-6 rounded-t-xl text-white">
                <div className="flex justify-between items-start">
                  <div>
                    <h2 className="text-2xl font-bold">{selectedPatient.name}</h2>
                    <p className="text-indigo-100">{selectedPatient.age} years • {selectedPatient.condition}</p>
                    <div className="flex items-center space-x-2 mt-2">
                      <MapPin className="w-4 h-4" />
                      <span className="text-sm text-indigo-100">{selectedPatient.location}</span>
                    </div>
                  </div>
                  <div className="text-right">
                    <span className={`px-4 py-2 rounded-full text-sm font-bold border-2 ${
                      selectedPatient.status === 'critical' ? 'bg-red-500 border-red-300' :
                      selectedPatient.status === 'high' ? 'bg-orange-500 border-orange-300' :
                      selectedPatient.status === 'moderate' ? 'bg-yellow-500 border-yellow-300' :
                      'bg-green-500 border-green-300'
                    }`}>
                      {selectedPatient.status.toUpperCase()}
                    </span>
                    <p className="text-sm text-indigo-100 mt-2">Risk Score: {selectedPatient.riskScore}/10</p>
                  </div>
                </div>
              </div>

              {/* Vital Signs */}
              <div className="p-6">
                <h3 className="text-lg font-bold text-gray-800 mb-4">Current Vital Signs</h3>
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-gradient-to-br from-red-50 to-red-100 p-5 rounded-xl border-2 border-red-200">
                    <div className="flex items-center space-x-3 mb-2">
                      <Heart className="w-6 h-6 text-red-600" />
                      <span className="text-sm font-medium text-gray-700">Heart Rate</span>
                    </div>
                    <p className="text-4xl font-bold text-red-700">{selectedPatient.hr}</p>
                    <p className="text-sm text-gray-600 mt-1">bpm • Baseline: 72</p>
                  </div>

                  <div className="bg-gradient-to-br from-blue-50 to-blue-100 p-5 rounded-xl border-2 border-blue-200">
                    <div className="flex items-center space-x-3 mb-2">
                      <Activity className="w-6 h-6 text-blue-600" />
                      <span className="text-sm font-medium text-gray-700">Blood Pressure</span>
                    </div>
                    <p className="text-4xl font-bold text-blue-700">{selectedPatient.bp}</p>
                    <p className="text-sm text-gray-600 mt-1">mmHg • Baseline: 120/80</p>
                  </div>

                  <div className="bg-gradient-to-br from-green-50 to-green-100 p-5 rounded-xl border-2 border-green-200">
                    <div className="flex items-center space-x-3 mb-2">
                      <Wind className="w-6 h-6 text-green-600" />
                      <span className="text-sm font-medium text-gray-700">Blood Oxygen</span>
                    </div>
                    <p className="text-4xl font-bold text-green-700">{selectedPatient.spo2}%</p>
                    <p className="text-sm text-gray-600 mt-1">SpO2 • Normal: 95-100%</p>
                  </div>

                  <div className="bg-gradient-to-br from-purple-50 to-purple-100 p-5 rounded-xl border-2 border-purple-200">
                    <div className="flex items-center space-x-3 mb-2">
                      <Thermometer className="w-6 h-6 text-purple-600" />
                      <span className="text-sm font-medium text-gray-700">Temperature</span>
                    </div>
                    <p className="text-4xl font-bold text-purple-700">{selectedPatient.temp}°C</p>
                    <p className="text-sm text-gray-600 mt-1">Body Temp • Normal: 36.5-37.5</p>
                  </div>
                </div>

                {/* AI Analysis */}
                <div className="mt-6 bg-gradient-to-r from-indigo-50 to-purple-50 p-6 rounded-xl border-2 border-indigo-200">
                  <div className="flex items-start space-x-3">
                    <div className="bg-indigo-500 p-2 rounded-lg">
                      <Activity className="w-5 h-5 text-white" />
                    </div>
                    <div className="flex-1">
                      <h4 className="font-bold text-indigo-900 mb-2">🤖 AI Health Analysis (IBM Granite)</h4>
                      {selectedPatient.status === 'critical' ? (
                        <div className="space-y-2 text-sm text-gray-700">
                          <p className="flex items-start space-x-2">
                            <AlertTriangle className="w-4 h-4 text-red-600 mt-0.5 flex-shrink-0" />
                            <span><strong>CRITICAL:</strong> Heart rate significantly elevated (125 bpm vs baseline 72 bpm) - 74% increase</span>
                          </p>
                          <p className="flex items-start space-x-2">
                            <AlertTriangle className="w-4 h-4 text-red-600 mt-0.5 flex-shrink-0" />
                            <span><strong>CRITICAL:</strong> Blood pressure in hypertensive crisis range (180/110) - immediate attention required</span>
                          </p>
                          <p className="flex items-start space-x-2">
                            <AlertTriangle className="w-4 h-4 text-red-600 mt-0.5 flex-shrink-0" />
                            <span><strong>CRITICAL:</strong> SpO2 below normal range (89%) indicating potential respiratory distress</span>
                          </p>
                          <div className="mt-3 pt-3 border-t border-indigo-200">
                            <p className="font-semibold text-red-700 flex items-center space-x-2">
                              <Zap className="w-4 h-4" />
                              <span>Emergency services notified • Ambulance dispatched • ETA: 4 minutes</span>
                            </p>
                          </div>
                        </div>
                      ) : (
                        <p className="text-sm text-gray-700">All vitals within acceptable ranges. Continue routine monitoring. Next scheduled check-in: 30 minutes.</p>
                      )}
                    </div>
                  </div>
                </div>

                {/* Device Info */}
                <div className="mt-4 flex items-center justify-between p-4 bg-gray-50 rounded-lg">
                  <div className="flex items-center space-x-2 text-sm text-gray-600">
                    <Clock className="w-4 h-4" />
                    <span>Last update: {selectedPatient.lastUpdate}</span>
                  </div>
                  <div className="flex items-center space-x-2 text-sm text-gray-600">
                    <Droplet className="w-4 h-4" />
                    <span>Device battery: {selectedPatient.deviceBattery}%</span>
                  </div>
                </div>

                {/* Action Buttons */}
                {userRole === 'doctor' && (
                  <div className="mt-6 grid grid-cols-2 gap-3">
                    <button className="bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition flex items-center justify-center space-x-2">
                      <User className="w-5 h-5" />
                      <span>View Full History</span>
                    </button>
                    <button className="bg-green-600 text-white py-3 rounded-lg font-semibold hover:bg-green-700 transition flex items-center justify-center space-x-2">
                      <Stethoscope className="w-5 h-5" />
                      <span>Update Care Plan</span>
                    </button>
                    <button className="bg-purple-600 text-white py-3 rounded-lg font-semibold hover:bg-purple-700 transition flex items-center justify-center space-x-2">
                      <Phone className="w-5 h-5" />
                      <span>Call Patient</span>
                    </button>
                    <button className="bg-gray-600 text-white py-3 rounded-lg font-semibold hover:bg-gray-700 transition flex items-center justify-center space-x-2">
                      <Calendar className="w-5 h-5" />
                      <span>Schedule Visit</span>
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* Recent Alerts */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-100 p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Recent System Alerts</h3>
              <div className="space-y-3">
                {alerts.map(alert => (
                  <div key={alert.id} className={`p-4 rounded-lg border-l-4 ${
                    alert.type === 'critical' ? 'border-red-500 bg-red-50' :
                    alert.type === 'high' ? 'border-orange-500 bg-orange-50' :
                    'border-blue-500 bg-blue-50'
                  }`}>
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center space-x-2 mb-1">
                          <span className="font-semibold text-gray-800">{alert.patient}</span>
                          <span className={`px-2 py-0.5 rounded-full text-xs font-semibold ${
                            alert.action === 'dispatched' ? 'bg-red-100 text-red-700' :
                            alert.action === 'notified' ? 'bg-orange-100 text-orange-700' :
                            'bg-blue-100 text-blue-700'
                          }`}>
                            {alert.action}
                          </span>
                        </div>
                        <p className="text-sm text-gray-700">{alert.message}</p>
                        <p className="text-xs text-gray-500 mt-1">{alert.time}</p>
                      </div>
                      <ChevronRight className="w-5 h-5 text-gray-400" />
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EnhancedDashboard;
