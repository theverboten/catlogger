import { Component, Input } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { error, info } from 'console';
import { HttpHeaders } from '@angular/common/http';
import { OnInit } from '@angular/core';
import { Message } from './message';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  /* baseURL: string = `http://localhost:3000/`; */

  title = 'Catlogger';
  displayVal: string = '';
  mess: Message = {
    id: 2,
    input: '',
  };
  info = '';

  getValue(val: string) {
    console.log(val);
    this.displayVal = val;
    this.mess.input = val;
    console.log(this.mess);
  }

  getMessage(input: string) {}

  sendData(data: string) {}

  constructor(private http: HttpClient) {}

  /*addMessage(): Observable<any> {
    const headers = { 'Content-type': 'application/json' };
    const body = this.mess;
    console.log(body);
    return this.http.post(`http://localhost:3000/inputData`, body, {
      headers: headers,
    });
  }*/
  addMessage(val: string) {
    this.mess.input = val;
    console.log(this.mess);
    this.http.put(`http://localhost:3000/inputData/2`, this.mess).subscribe(
      (data) => {
        console.log(`Post request is succesfull `, data);
      },
      (error) => {
        console.log(`Error: `, error);
      }
    );
  }

  getInfo() {
    this.http.get(`http://127.0.0.1:5000/get`).subscribe(
      (data) => {
        console.log(`Get request is succesfull `, data);
      },
      (error) => {
        console.log(`Error: `, error);
      }
    );
  }

  getConvert() {
    this.http.get(`http://127.0.0.1:5000/convert`).subscribe(
      (data) => {
        console.log(`Get request is succesfull `, data);
      },
      (error) => {
        console.log(`Error: `, error);
      }
    );
  }
}
