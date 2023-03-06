"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.pluginService = exports.PluginService = void 0;
const CustomConsole_1 = require("@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole");
class PluginService {
    constructor() {
        this.pluginConfig = window.pluginConfig;
        this._portAddress = window.javaConnector.getPortNumber();
        try {
            this._initArgs = this.pluginConfig.initArgs();
        }
        catch (errr) {
            (0, CustomConsole_1.log)('init args error : ' + errr);
            this._initArgs = new Map();
            return;
        }
    }
    readJSONAsync(url) {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const response = yield fetch(url);
                const json = yield response.json();
                (0, CustomConsole_1.log)('Successfully read JSON from ' + url);
                return json;
            }
            catch (err) {
                (0, CustomConsole_1.error)('Unable to fetch URL : ' + url + '\n' + err);
            }
        });
    }
    absolutePath(relativePath) {
        return this.frameworkRoot() + '/' + relativePath;
    }
    frameworkRoot() {
        const { protocol, host } = document.location;
        return protocol + '//' + host;
    }
    openURL(relativePath) {
        window.open(this.absolutePath(relativePath), '_blank', 'toolbar=0,location=0,menubar=0');
    }
    readJSON(path) {
        const request = new XMLHttpRequest();
        request.open('GET', path, false);
        request.send(null);
        if (request.status === 200) {
            return JSON.parse(request.responseText);
        }
        else {
            throw new Error('Unable to read url : ' + path);
        }
    }
    get initArgs() {
        return this._initArgs;
    }
    get portAddress() {
        return this._portAddress;
    }
}
exports.PluginService = PluginService;
exports.pluginService = new PluginService();
