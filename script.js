let currentMode = "";
let caseData = {};

document.getElementById('patient-btn').onclick = () => {
    document.getElementById('home-screen').style.display = 'none';
    document.getElementById('mode-screen').style.display = 'block';
};

function loadCases(mode) {
    currentMode = mode;
    fetch(`/api/cases/${mode}`).then(res => res.json()).then(data => {
        caseData = data;
        document.getElementById('mode-screen').style.display = 'none';
        document.getElementById('case-screen').style.display = 'block';
        const keys = mode === 'emergency' ? Object.keys(data) : data;
        document.getElementById('case-list').innerHTML = `<h2>${mode.toUpperCase()} CASES</h2>` + 
            keys.map(c => `<div class="login-card" style="width:100%" onclick="loadHospitals('${c}')">${c}</div>`).join('');
    });
}

function loadHospitals(c) {
    fetch('/api/hospitals').then(res => res.json()).then(hospitals => {
        document.getElementById('case-screen').style.display = 'none';
        document.getElementById('hospital-screen').style.display = 'block';
        
        if(currentMode === 'emergency') {
            document.getElementById('aid-box').style.display = 'block';
            document.getElementById('aid-box').innerHTML = `<h3 style="color:red">🚨 First Aid Instructions:</h3><p>${caseData[c]}</p>`;
        } else {
            document.getElementById('aid-box').style.display = 'none';
        }

        document.getElementById('hospital-list').innerHTML = hospitals.map(h => {
            // Calculate time difference for "Last Updated"
            const lastUpdate = new Date(h.updated_at);
            const diff = Math.floor((new Date() - lastUpdate) / 60000); 

            return `
            <div class="h-card" style="padding:20px; border-radius:15px; background:white; margin-bottom:15px; box-shadow:0 4px 6px rgba(0,0,0,0.1)">
                <h2 style="color:#2d3748">${h.name}</h2>
                <p><strong>👨‍⚕️ Doctor:</strong> ${h.doctor} (${h.specialty})</p>
                <p><strong>🛏️ ICU Beds Available:</strong> ${h.icu_beds}</p>
                <p style="color:gray; font-size:12px;">🕒 Last updated: ${diff} minutes ago</p>
                <hr style="margin:10px 0">
                <div style="display:flex; gap:10px; flex-wrap:wrap;">
                    <button class="btn-n" style="width:auto; padding:8px 15px;" onclick="window.open('https://www.google.com/maps?q=${h.lat},${h.lng}')">📍 Map Location</button>
                    <button class="btn-n" style="width:auto; padding:8px 15px; background:#4a5568" onclick="alert('Calling Hospital: ${h.phone}')">📞 Call Hospital</button>
                    
                    ${(currentMode === 'emergency' && h.amb_available) ? `
                        <button class="btn-e" style="width:auto; padding:8px 15px; margin:0" onclick="startTracking('${h.name}', '${h.lat}', '${h.lng}')">🚑 Call & Track Ambulance</button>
                    ` : ''}
                </div>
            </div>`;
        }).join('');
    });
}

function startTracking(hName, lat, lng) {
    alert(`Ambulance Dispatched from ${hName}!\nCalling: 911\n\nOpening GPS Tracking...`);
    // Opens a simulated tracking view using coordinates
    window.open(`https://maps.google.com/maps?q=$${lat},${lng}&t=&z=15&ie=UTF8&iwloc=&output=embed`);
}