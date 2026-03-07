// Stubbed MFS100 library for Fingerprint Bypass
var uri = "";
var KeyFlag = "";
var isGetSuccess = true;

function GetMFS100Info() {
    return { httpStaus: true, data: { ErrorCode: "0", ErrorDescription: "Success (Bypass Mode)" } };
}

function GetMFS100KeyInfo(key) {
    return { httpStaus: true, data: { ErrorCode: "0", ErrorDescription: "Success (Bypass Mode)" } };
}

function CaptureFinger(quality, timeout) {
    return {
        httpStaus: true,
        data: {
            ErrorCode: "0",
            ErrorDescription: "Success (Bypass Mode)",
            BitmapData: "",
            IsoTemplate: "MOCK_DATA"
        }
    };
}

function VerifyFinger(ProbFMR, GalleryFMR) {
    return { httpStaus: true, data: { Status: true, ErrorCode: "0", ErrorDescription: "Success (Bypass Mode)" } };
}

function MatchFinger(quality, timeout, GalleryFMR) {
    return { httpStaus: true, data: { Status: true, ErrorCode: "0", ErrorDescription: "Success (Bypass Mode)" } };
}

function GetPidData(BiometricArray) { return { httpStaus: true, data: { ErrorCode: "0" } }; }
function GetProtoPidData(BiometricArray) { return { httpStaus: true, data: { ErrorCode: "0" } }; }
function GetRbdData(BiometricArray) { return { httpStaus: true, data: { ErrorCode: "0" } }; }
function GetProtoRbdData(BiometricArray) { return { httpStaus: true, data: { ErrorCode: "0" } }; }

function PostMFS100Client(method, jsonData) { return { httpStaus: true, data: {} }; }
function GetMFS100Client(method) { return { httpStaus: true, data: {} }; }
function getHttpError(jqXHR) { return "Success (Bypass Mode)"; }

function Biometric(BioType, BiometricData, Pos, Nfiq, Na) {
    this.BioType = BioType;
    this.BiometricData = BiometricData;
    this.Pos = Pos;
    this.Nfiq = Nfiq;
    this.Na = Na;
}

function MFS100Request(BiometricArray) {
    this.Biometrics = BiometricArray;
}

function PrepareScanner() { return true; }
function getFalseRes() { return { httpStaus: true, data: {} }; }