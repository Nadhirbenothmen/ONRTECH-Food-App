import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterConsumerComponent } from './register-consumer.component';

describe('RegisterConsumerComponent', () => {
  let component: RegisterConsumerComponent;
  let fixture: ComponentFixture<RegisterConsumerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegisterConsumerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegisterConsumerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
