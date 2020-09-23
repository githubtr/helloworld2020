
import {Component, ViewEncapsulation} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  encapsulation: ViewEncapsulation.Emulated
})
export class AppComponent {
  name: string;
  title: string;

  constructor() {
    this.name = 'World - Angular 10.1.2 is really fun!';
    this.title = 'HelloWorld';
  }
}
